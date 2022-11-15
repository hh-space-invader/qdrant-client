# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import snapshots_service_pb2 as snapshots__service__pb2


class SnapshotsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/qdrant.Snapshots/Create',
                request_serializer=snapshots__service__pb2.CreateSnapshotRequest.SerializeToString,
                response_deserializer=snapshots__service__pb2.CreateSnapshotResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/qdrant.Snapshots/List',
                request_serializer=snapshots__service__pb2.ListSnapshotsRequest.SerializeToString,
                response_deserializer=snapshots__service__pb2.ListSnapshotsResponse.FromString,
                )
        self.CreateFull = channel.unary_unary(
                '/qdrant.Snapshots/CreateFull',
                request_serializer=snapshots__service__pb2.CreateFullSnapshotRequest.SerializeToString,
                response_deserializer=snapshots__service__pb2.CreateSnapshotResponse.FromString,
                )
        self.ListFull = channel.unary_unary(
                '/qdrant.Snapshots/ListFull',
                request_serializer=snapshots__service__pb2.ListFullSnapshotsRequest.SerializeToString,
                response_deserializer=snapshots__service__pb2.ListSnapshotsResponse.FromString,
                )


class SnapshotsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """
        Create collection snapshot
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """
        List collection snapshots
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFull(self, request, context):
        """
        Create full storage snapshot
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFull(self, request, context):
        """
        List full storage snapshots
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SnapshotsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=snapshots__service__pb2.CreateSnapshotRequest.FromString,
                    response_serializer=snapshots__service__pb2.CreateSnapshotResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=snapshots__service__pb2.ListSnapshotsRequest.FromString,
                    response_serializer=snapshots__service__pb2.ListSnapshotsResponse.SerializeToString,
            ),
            'CreateFull': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFull,
                    request_deserializer=snapshots__service__pb2.CreateFullSnapshotRequest.FromString,
                    response_serializer=snapshots__service__pb2.CreateSnapshotResponse.SerializeToString,
            ),
            'ListFull': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFull,
                    request_deserializer=snapshots__service__pb2.ListFullSnapshotsRequest.FromString,
                    response_serializer=snapshots__service__pb2.ListSnapshotsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'qdrant.Snapshots', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Snapshots(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Snapshots/Create',
            snapshots__service__pb2.CreateSnapshotRequest.SerializeToString,
            snapshots__service__pb2.CreateSnapshotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Snapshots/List',
            snapshots__service__pb2.ListSnapshotsRequest.SerializeToString,
            snapshots__service__pb2.ListSnapshotsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateFull(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Snapshots/CreateFull',
            snapshots__service__pb2.CreateFullSnapshotRequest.SerializeToString,
            snapshots__service__pb2.CreateSnapshotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListFull(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Snapshots/ListFull',
            snapshots__service__pb2.ListFullSnapshotsRequest.SerializeToString,
            snapshots__service__pb2.ListSnapshotsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)