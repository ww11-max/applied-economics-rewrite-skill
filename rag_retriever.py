#!/usr/bin/env python3
"""
RAG Retriever for Applied Economics Writing Skill
===================================================
Retrieves the most stylistically relevant published AE exemplars
for a given draft text, filtered by chapter type.

Usage:
    python rag_retriever.py --chapter-type abstract --query "draft text here"
    python rag_retriever.py --chapter-type introduction --top-k 5 --query "draft text"
    python rag_retriever.py --chapter-type results --query-file draft.txt

Dependencies:
    pip install sentence-transformers faiss-cpu numpy
"""

import argparse
import json
import os
import sys
import numpy as np

# ---- Paths (relative to repo root) ----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSONL_PATH = os.path.join(BASE_DIR, "data", "economics_papers_vectors.jsonl")
INDEX_PATH = os.path.join(BASE_DIR, "data", "economics_papers.index")
META_PATH = os.path.join(BASE_DIR, "data", "economics_papers_meta.json")

# Mapping: simplified (JSONL) → metadata chapter type names
CHAPTER_TYPE_MAP = {
    "abstract": "abstract",
    "introduction": "introduction",
    "review": "literature_review",
    "literature_review": "literature_review",
    "model": "theoretical_model",
    "theoretical_model": "theoretical_model",
    "variables": "data_and_variables",
    "data_and_variables": "data_and_variables",
    "results": "empirical_results",
    "empirical_results": "empirical_results",
    "robustness": "robustness",
    "conclusion": "conclusion",
}

VALID_CHAPTER_TYPES = set(CHAPTER_TYPE_MAP.keys())


class AERetriever:
    """Retrieve Applied Economics paper exemplars via FAISS + sentence-transformers."""

    def __init__(self, model_name: str = "all-mpnet-base-v2"):
        self.model_name = model_name
        self.model = None
        self.index = None
        self.metadata = None
        self.records = None

    def load(self):
        """Load the embedding model, FAISS index, metadata, and JSONL records."""
        from sentence_transformers import SentenceTransformer
        import faiss

        print(f"[RAG] Loading model: {self.model_name}...")
        self.model = SentenceTransformer(self.model_name)

        print(f"[RAG] Loading FAISS index: {INDEX_PATH}")
        self.index = faiss.read_index(INDEX_PATH)

        print(f"[RAG] Loading metadata: {META_PATH}")
        with open(META_PATH, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

        print(f"[RAG] Loading JSONL records: {JSONL_PATH}")
        self.records = []
        with open(JSONL_PATH, "r", encoding="utf-8") as f:
            for line in f:
                self.records.append(json.loads(line))

        print(f"[RAG] Ready. {len(self.records)} records, "
              f"{self.index.ntotal} vectors, dim={self.index.d}")

    def retrieve(self, query_text: str, chapter_type: str = None, top_k: int = 5):
        """
        Retrieve top-k most similar AE exemplars.

        Args:
            query_text: The draft text to find exemplars for.
            chapter_type: Filter to specific chapter type (accepts both simplified
                          and metadata names; None = no filter).
            top_k: Number of results to return.

        Returns:
            List of dicts with keys: text, source, chapter_type, distance.
        """
        # Map user-facing chapter type to metadata chapter type
        if chapter_type:
            chapter_type = CHAPTER_TYPE_MAP.get(chapter_type, chapter_type)

        if self.model is None:
            self.load()

        query_vec = self.model.encode([query_text])
        search_k = max(top_k * 5, 20)
        distances, indices = self.index.search(
            query_vec.astype(np.float32), search_k
        )

        results = []
        for i, idx in enumerate(indices[0]):
            if idx < 0 or idx >= len(self.metadata):
                continue

            meta = self.metadata[idx]
            rec_idx = meta.get("index_id", idx)
            if rec_idx >= len(self.records):
                continue

            rec = self.records[rec_idx]
            ct = meta.get("chapter_type", rec["id"].rsplit("_", 2)[-2])

            if chapter_type and ct != chapter_type:
                continue

            results.append({
                "text": rec["text_chunk"],
                "source": rec["id"],
                "chapter_type": ct,
                "distance": float(distances[0][i]),
            })

            if len(results) >= top_k:
                break

        return results

    def show_chapter_stats(self):
        """Print chapter type distribution in the vector DB."""
        if self.metadata is None:
            self.load()
        from collections import Counter
        cts = Counter(m["chapter_type"] for m in self.metadata)
        print("\n[RAG] Chapter type distribution (metadata names):")
        for ct, count in cts.most_common():
            print(f"  {ct}: {count}")


def main():
    parser = argparse.ArgumentParser(
        description="RAG Retriever for Applied Economics Writing Skill"
    )
    parser.add_argument(
        "--chapter-type", "-c", type=str, default=None,
        choices=list(VALID_CHAPTER_TYPES) + [None],
        help="Filter results to specific chapter type"
    )
    parser.add_argument(
        "--top-k", "-k", type=int, default=5,
        help="Number of exemplars to retrieve (default: 5)"
    )
    parser.add_argument(
        "--query", "-q", type=str, default=None,
        help="Query text (draft to find exemplars for)"
    )
    parser.add_argument(
        "--query-file", "-f", type=str, default=None,
        help="Read query from file"
    )
    parser.add_argument(
        "--stats", action="store_true",
        help="Show chapter distribution statistics"
    )
    parser.add_argument(
        "--output", "-o", type=str, default=None,
        help="Save results to JSON file"
    )

    args = parser.parse_args()

    retriever = AERetriever()

    if args.stats:
        retriever.show_chapter_stats()
        return

    # Get query
    if args.query_file:
        with open(args.query_file, "r", encoding="utf-8") as f:
            query = f.read().strip()
    elif args.query:
        query = args.query
    else:
        print("ERROR: Provide --query or --query-file")
        sys.exit(1)

    if not query:
        print("ERROR: Empty query")
        sys.exit(1)

    # Retrieve
    results = retriever.retrieve(
        query_text=query,
        chapter_type=args.chapter_type,
        top_k=args.top_k,
    )

    print(f"\n[RAG] Retrieved {len(results)} exemplars "
          f"(chapter_type={args.chapter_type or 'all'})")
    print("=" * 70)

    for i, r in enumerate(results):
        print(f"\n--- Exemplar {i+1} | {r['chapter_type']} | "
              f"distance={r['distance']:.4f}")
        print(f"    Source: {r['source']}")
        print(f"    Text preview: {r['text'][:300]}...")

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\nResults saved to: {args.output}")


if __name__ == "__main__":
    main()
