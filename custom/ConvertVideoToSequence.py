__version__ = "1.0"

from meshroom.core import desc


class ConvertVideoToSequence(desc.CommandLineNode):
    category = "Custom"
    documentation = """This node converts a video into a sequence of images using FFMPEG."""

    inputs = [
        desc.File(
            name="inputFile",
            label="Input File",
            description="Input video to convert into a sequence of images.",
            value="",
            uid=[0]
        ),
        desc.IntParam(
            name="fps",
            label="Framerate",
            description="Framerate of the output sequence.",
            value=24,
            range=(1, 1000, 1),
            uid=[0]
        ),
        desc.StringParam(
            name="outputPattern",
            label="Output Pattern",
            description="Output pattern for the sequence of images. Use '%d' to specify the frame number.",
            value="out%d.png",
            uid=[0]
        )
    ]

    outputs = [
        desc.File(
            name='outputSequence',
            label='Output Sequence',
            description="Generated sequence.",
            value=desc.Node.internalFolder,
            semantic="sequence",
            uid=[]
        )
    ]

    def processChunk(self, chunk):
        inputValue = "{inputFileValue}"
        framerateValue = "{fpsValue}"
        outputPatternValue = "{outputSequenceValue}/{outputPatternValue}"

        # Objective is to convert a video into a sequence of images
        # ffmpeg -i input.flv -vf fps=24 out%d.png
        self.commandLine = "ffmpeg -i " + inputValue + " -vf fps=" + framerateValue + " " + outputPatternValue

        desc.CommandLineNode.processChunk(self, chunk)

