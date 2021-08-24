import core.error


class COLORObject(object):
    def __init__(self):
        pass


class BGObject(object):
    TypeList = ["color", "video", "picture"]
    KeyWordDict = dict(video="videofilename", picture="picturefilename", color="color")

    def __init__(self, bgtype="color", **keywords):
        self.type = bgtype
        if self.type not in self.TypeList:
            raise core.error.L4STypeError("Can not find {0} type for Background. ".format(self.type))
        # for keyword in keywords:
        # if self.KeyWordDict[]


class LYRICObject(object):
    def __init__(self, font):
        pass


class L4SUI(object):
    def __init__(self):
        pass

    def backgroundShow(self, background):
        pass

    def lyricsShow(self, lyrics):
        pass

    def start(self):
        pass

    def end(self):
        pass
