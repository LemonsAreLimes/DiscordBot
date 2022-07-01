class r34():
    async def pron(tags):
        import rule34
        rule34 = await rule34.Sync()

        req = await rule34.getImages(tags=tags)

        return req
