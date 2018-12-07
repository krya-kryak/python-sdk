# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.mdb.postgresql.v1 import cluster_pb2 as yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__pb2
from yandex.cloud.mdb.postgresql.v1 import cluster_service_pb2 as yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class ClusterServiceStub(object):
  """A set of methods for managing PostgreSQL Cluster resources.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/yandex.cloud.mdb.postgresql.v1.ClusterService/Get',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.GetClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__pb2.Cluster.FromString,
        )
    self.List = channel.unary_unary(
        '/yandex.cloud.mdb.postgresql.v1.ClusterService/List',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClustersRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClustersResponse.FromString,
        )
    self.Create = channel.unary_unary(
        '/yandex.cloud.mdb.postgresql.v1.ClusterService/Create',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.CreateClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Update = channel.unary_unary(
        '/yandex.cloud.mdb.postgresql.v1.ClusterService/Update',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.UpdateClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Delete = channel.unary_unary(
        '/yandex.cloud.mdb.postgresql.v1.ClusterService/Delete',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.DeleteClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Backup = channel.unary_unary(
        '/yandex.cloud.mdb.postgresql.v1.ClusterService/Backup',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.BackupClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Restore = channel.unary_unary(
        '/yandex.cloud.mdb.postgresql.v1.ClusterService/Restore',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.RestoreClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.ListLogs = channel.unary_unary(
        '/yandex.cloud.mdb.postgresql.v1.ClusterService/ListLogs',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterLogsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterLogsResponse.FromString,
        )
    self.ListOperations = channel.unary_unary(
        '/yandex.cloud.mdb.postgresql.v1.ClusterService/ListOperations',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterOperationsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterOperationsResponse.FromString,
        )
    self.ListBackups = channel.unary_unary(
        '/yandex.cloud.mdb.postgresql.v1.ClusterService/ListBackups',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterBackupsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterBackupsResponse.FromString,
        )
    self.ListHosts = channel.unary_unary(
        '/yandex.cloud.mdb.postgresql.v1.ClusterService/ListHosts',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterHostsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterHostsResponse.FromString,
        )
    self.AddHosts = channel.unary_unary(
        '/yandex.cloud.mdb.postgresql.v1.ClusterService/AddHosts',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.AddClusterHostsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.DeleteHosts = channel.unary_unary(
        '/yandex.cloud.mdb.postgresql.v1.ClusterService/DeleteHosts',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.DeleteClusterHostsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.UpdateHosts = channel.unary_unary(
        '/yandex.cloud.mdb.postgresql.v1.ClusterService/UpdateHosts',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.UpdateClusterHostsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )


class ClusterServiceServicer(object):
  """A set of methods for managing PostgreSQL Cluster resources.
  """

  def Get(self, request, context):
    """Returns the specified PostgreSQL Cluster resource.

    To get the list of available PostgreSQL Cluster resources, make a [List] request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """Retrieves the list of PostgreSQL Cluster resources that belong
    to the specified folder.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    """Creates a PostgreSQL cluster in the specified folder.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Updates the specified PostgreSQL cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Deletes the specified PostgreSQL cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Backup(self, request, context):
    """Creates a backup for the specified PostgreSQL cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Restore(self, request, context):
    """Creates a new PostgreSQL cluster using the specified backup.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListLogs(self, request, context):
    """Retrieves logs for the specified PostgreSQL cluster.
    For more information about logs, see the [Logs](/docs/yandex-mdb-guide/concepts/logs) section in the Developer's Guide.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListOperations(self, request, context):
    """Retrieves the list of Operation resources for the specified cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListBackups(self, request, context):
    """Retrieves the list of available backups for the specified PostgreSQL cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListHosts(self, request, context):
    """Retrieves a list of hosts for the specified cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddHosts(self, request, context):
    """Creates new hosts for a cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteHosts(self, request, context):
    """Deletes the specified hosts for a cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateHosts(self, request, context):
    """Updates the specified hosts.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ClusterServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.GetClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__pb2.Cluster.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClustersRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClustersResponse.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.CreateClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.UpdateClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.DeleteClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Backup': grpc.unary_unary_rpc_method_handler(
          servicer.Backup,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.BackupClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Restore': grpc.unary_unary_rpc_method_handler(
          servicer.Restore,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.RestoreClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'ListLogs': grpc.unary_unary_rpc_method_handler(
          servicer.ListLogs,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterLogsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterLogsResponse.SerializeToString,
      ),
      'ListOperations': grpc.unary_unary_rpc_method_handler(
          servicer.ListOperations,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterOperationsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterOperationsResponse.SerializeToString,
      ),
      'ListBackups': grpc.unary_unary_rpc_method_handler(
          servicer.ListBackups,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterBackupsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterBackupsResponse.SerializeToString,
      ),
      'ListHosts': grpc.unary_unary_rpc_method_handler(
          servicer.ListHosts,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterHostsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.ListClusterHostsResponse.SerializeToString,
      ),
      'AddHosts': grpc.unary_unary_rpc_method_handler(
          servicer.AddHosts,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.AddClusterHostsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'DeleteHosts': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteHosts,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.DeleteClusterHostsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'UpdateHosts': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateHosts,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_cluster__service__pb2.UpdateClusterHostsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.mdb.postgresql.v1.ClusterService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
