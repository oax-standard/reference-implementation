# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbs

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Checkpoint(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCheckpoint(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Checkpoint()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def CheckpointBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4F\x44\x54\x43", size_prefixed=size_prefixed)

    # Checkpoint
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Checkpoint
    def Version(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Checkpoint
    def ModuleState(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from ort_flatbuffers_py.fbs.ModuleState import ModuleState
            obj = ModuleState()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Checkpoint
    def OptimizerGroups(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from ort_flatbuffers_py.fbs.OptimizerGroup import OptimizerGroup
            obj = OptimizerGroup()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Checkpoint
    def OptimizerGroupsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Checkpoint
    def OptimizerGroupsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # Checkpoint
    def PropertyBag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from ort_flatbuffers_py.fbs.PropertyBag import PropertyBag
            obj = PropertyBag()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def CheckpointStart(builder): builder.StartObject(4)
def CheckpointAddVersion(builder, version): builder.PrependInt32Slot(0, version, 0)
def CheckpointAddModuleState(builder, moduleState): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(moduleState), 0)
def CheckpointAddOptimizerGroups(builder, optimizerGroups): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(optimizerGroups), 0)
def CheckpointStartOptimizerGroupsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CheckpointAddPropertyBag(builder, propertyBag): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(propertyBag), 0)
def CheckpointEnd(builder): return builder.EndObject()
