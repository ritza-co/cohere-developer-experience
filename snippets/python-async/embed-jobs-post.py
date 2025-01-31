import cohere
import asyncio

co = cohere.AsyncClient("<<apiKey>>")


async def main():
    # start an embed job
    response = await co.embed_jobs.create(
        dataset_id=ds.id, input_type="search_document", model="embed-english-v3.0"
    )

    # poll the server until the job is complete
    response = await co.wait(job)

    print(response)

asyncio.run(main())
