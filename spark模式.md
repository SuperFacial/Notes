### Spark 运行模式
Spark 的运行模式多种多样、灵活多变，部署在单机上时，既可以用本地模式运行，也可以用伪分布式模式运行，而当以分布式集群的方式部署时，也有众多的运行模式可以供选择，这取决于集群的实际情况，底层的资源调度既可以依赖于外部的资源调度框架，也可以使用 Spark 内建的 Standalone 模式。对于外部资源调度框架的支持，目前的实现包括相对稳定的 Mesos 模式，以及还在持续开发更新中的 Hadoop YARN 模式。

在实际应用中，Spark 应用程序的运行模式取决于传递给 SparkContext 的 MASTER 环境变量的值，个别模式还需要依赖辅助的程序接口来配合使用，目前所支持的 MASTER 环境变量由特定的字符串或 URL 所组成。例如：

Local[N]：本地模式，使用 N 个线程。

Local Cluster[Worker,core,Memory]：伪分布式模式，可以配置所需要启动的虚拟工作节点的数量，以及每个工作节点所管理的 CPU 数量和内存尺寸。

Spark://hostname:port:Standalone 模式，需要部署 Spark 到相关节点，URL 为 Spark Master 主机地址和端口。

Mesos://hostname:port:Mesos 模式，需要部署 Spark 和 Mesos 到相关节点，URL 为 Mesos 主机地址和端口。

YARN standalone/Yarn cluster:YARN 模式一，主程序逻辑和任务都运行在 YARN 集群中。

YARN client:YARN 模式二，主程序逻辑运行在本地，具体任务运行在 YARN 集群中。
