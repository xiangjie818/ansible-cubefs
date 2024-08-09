#### 修改hosts
一共master（管理节点），meta（元数据节点），data（数据节点），object（对象存储节点）四种组件，将节点要安装的设置为True
```
[cubefs]
10.130.100.36 master=True meta=True data=True object=True
10.130.100.37 master=True meta=True data=True object=True
10.130.100.38 master=True meta=True data=True object=True

[consul]
10.130.100.36
10.130.100.37
10.130.100.38

[all:vars]
ansible_ssh_port=22
```
#### 修改group_vars/all.yaml
配置示例如下
```
# 配置CubeFS安装信息
cubefs_package: cubefs-3.3.0-linux-amd64.tar.gz
download_site: http://s3.jishu.idc/spider-internal-read/cubefs/
cluster_name: cubefs_cold

# 配置数据盘的挂载路径
mountmap:
  /dev/sdb:
    directory: /cfs/data1
  /dev/sdc:
    directory: /cfs/data2
  /dev/sdd:
    directory: /cfs/data3
  /dev/sde:
    directory: /cfs/data4
  /dev/sdf:
    directory: /cfs/data5
  /dev/sdg:
    directory: /cfs/data6
  /dev/sdh:
    directory: /cfs/data7
  /dev/sdi:
    directory: /cfs/data8
```
支持的配置参数
| 参数 | 默认值 |
| -- | --|
|cubefs_dir | /opt/cubefs |
|cubefs_conf | {{ cubefs_dir }}/conf |
|cubefs_log | {{ cubefs_dir }}/log |
|consul_addr | http://cfsconsul.paas.idc |
|cubefs_master_dir | {{ cubefs_dir }}/master |
|cubefs_master_port | 17010 |
|cubefs_master_prof | 17020 |
|cubefs_master_retainLogs | 20000 |
|cubefs_master_logLevel | info |
|cubefs_master_metaNodeReservedMem | 1073741824 |
|cubefs_master_logDir | {{ cubefs_log }}/master |
|cubefs_master_walDir | {{ cubefs_master_dir }}/wal |
|cubefs_master_storeDir| {{ cubefs_master_dir }}/store |
|cubefs_meta_dir| {{ cubefs_dir }}/metadata |
|cubefs_meta_port| 17210 |
|cubefs_meta_prof| 17220 |
|cubefs_meta_raftHeartbeatPort| 17230 |
|cubefs_meta_raftReplicaPort| 17240 |
|cubefs_meta_exporterPort| 9501 |
|cubefs_meta_logLevel| info |
|cubefs_meta_logDir| {{ cubefs_log }}/metadata |
|cubefs_meta_metadataDir| {{ cubefs_meta_dir }}/meta |
|cubefs_meta_raftDir| {{ cubefs_meta_dir }}/raft |
|cubefs_meta_totalMem| 2147483648 |
|cubefs_data_dir| {{ cubefs_dir }}/datanode |
|cubefs_data_port| 17310 |
|cubefs_data_prof| 17320 |
|cubefs_data_raftHeartbeat| 17330 |
|cubefs_data_raftReplica| 17340 |
|cubefs_data_exporterPort| 9502 |
|cubefs_data_logLevel| info |
|cubefs_data_logDir| {{ cubefs_log }}/datanode |
|cubefs_data_raftDir| {{ cubefs_data_dir }}/raft |
|cubefs_data_reservedspace| 1073741824 |
|cubefs_object_dir| {{ cubefs_dir }}/objectnode |
|cubefs_object_port| 17410 |
|cubefs_object_prof| 17420 |
|cubefs_object_exporterPort| 9503 |
|cubefs_object_logLevel| info |
|cubefs_object_logDir| {{ cubefs_log }}/objectnode |
|cubefs_object_domains| test.cfs.local |
|consul_package |consul_1.15.2_linux_amd64.tar.gz |
|consul_download_site |http://s3.jishu.idc/spider-internal-read/consul |
|consul_download_url |'{{ consul_download_site }}/{{ consul_package }}' |
|consul_basedir | /opt/consul |
|consul_datadir |'{{ consul_basedir }}/data' |
|consul_confdir |'{{ consul_basedir }}/consul.d' |
#### 开始安装
```
ansible-playbook cubefs.yaml -i hosts
```
