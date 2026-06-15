# from pipeline import ingest
# from chroma import query_chunks

# result = ingest("https://github.com/NotKshitiz/rag-from-scratch")
# print(result)

# try:
#     results = query_chunks(
#         "rag-from-scratch",
#         "how does similarity search work?"
#     )
#     print(results)
# except Exception as e:
#     print("QUERY ERROR:", e)

from chat import ask_repo as ask

answer = ask("rag-from-scratch", "how does similarity search work?")
print(answer)