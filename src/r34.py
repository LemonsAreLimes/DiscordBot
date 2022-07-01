class r34():
    def pron(tags):
        import rule34
        rule34 = rule34.Sync()

        req = rule34.getImages(tags=tags)

        return req
