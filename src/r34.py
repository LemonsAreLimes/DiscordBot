import rule34


async def pron(tags):
    rule34 = await rule34.Sync()
    req = await rule34.getImages(tags=tags)
    return req
