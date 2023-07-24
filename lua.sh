如果你有Lua源代码的tar.gz包，并且想要编译并安装到指定的目录（例如`/home/lua`）

首先，确保你已经安装了编译工具（如gcc）和`readline`库，这是编译Lua所必需的。在Debian或Ubuntu上，你可以通过以下命令安装：

```bash
sudo apt-get install build-essential libreadline-dev
```

然后，按照以下步骤编译和安装Lua：

1. 解压源码包：

```bash
tar -xzvf lua-5.4.6.tar.gz
cd lua-5.4.6
```

2. 在编译前，你需要修改`Makefile`以指定安装位置。找到`Makefile`中的`INSTALL_TOP`变量，并将其设置为你的目标目录（例如`/home/lua`）。

你可以使用`sed`命令来修改`Makefile`：

```bash
sed -i 's|INSTALL_TOP= /usr/local|INSTALL_TOP= /home/nan/lua|' Makefile
```

3. 编译源码：

```bash
make linux test
```

4. 安装Lua到指定的目录：

```bash
make install
```

此时，Lua应该已经被安装到了`/home/lua`目录。

为了在其他机器上也能使用这个Lua环境，你需要把`/home/lua`目录打包并复制到目标机器，然后解压。你也需要把`/home/lua/bin`添加到目标机器的`PATH`环境变量中。

你可以通过修改`~/.bashrc`或`~/.bash_profile`文件来添加环境变量，在文件的末尾添加以下行：

```bash
export PATH=/home/lua/bin:$PATH
```

然后，运行下面的命令使改动生效：

```bash
source ~/.bashrc  # 或者 source ~/.bash_profile
```

这样，你就可以在新的机器上使用这个Lua环境了。
docker-ce/focal 5:19.03.9~3-0~ubuntu-focal amd64

sudo apt install docker-ce/focal 5:19.03.9~3-0~ubuntu-focal amd64 docker-ce-cli=docker-ce/focal 5:19.03.9~3-0~ubuntu-focal amd64 containerd.io


This command is used to install specific versions of Docker on a system running a Debian-based Linux distribution, such as Ubuntu.

To use this command, replace `<VERSION>` with the specific version number of Docker you want to install. For example:

```
sudo apt install docker-ce=19.03.13~3-0~ubuntu-bionic docker-ce-cli=19.03.13~3-0~ubuntu-bionic containerd.io
```

In this example, version 19.03.13 is being installed.

Note that the specific version numbers may vary depending on the version available in the package repository and the Linux distribution being used. You can check the available versions by running `apt-cache madison docker-ce`.


似乎你正在尝试安装特定版本的 Docker，但是 APT 包管理器找不到该版本。这可能是由于该版本在你的 APT 源中不存在，或者你的 APT 源尚未更新到最新状态。

首先，你可以尝试更新 APT 源的索引，然后再次尝试安装，步骤如下：

```bash
sudo apt-get update
sudo apt-get install docker-ce=19.03.13~3-0~ubuntu-bionic docker-ce-cli=19.03.13~3-0~ubuntu-bionic containerd.io
```

如果这仍然不起作用，那么可能是你的 APT 源中没有你想要的 Docker 版本。你可以使用以下命令查看 APT 源中可用的 Docker 版本：

```bash
apt-cache madison docker-ce
```

这将列出 APT 源中所有可用的 Docker 版本。你可以从这个列表中选择一个可用的版本进行安装。

如果你的 APT 源中没有你想要的版本，那么你可能需要添加一个包含该版本的新 APT 源。 对于 Docker，你可以按照 [Docker 官方文档 ↗](https://docs.docker.com/engine/install/ubuntu/)中的说明添加官方的 Docker APT 源。

最后，关于 `WARNING: apt does not have a stable CLI interface. Use with caution in scripts.` 警告，这是因为 `apt` 的命令行接口并不稳定，因此在脚本中使用可能会有风险。在脚本中，你应该使用 `apt-get` 或 `apt-cache` 而不是 `apt`。




根据你提供的信息，你的 APT 源中并没有 `docker-ce=19.03.13~3-0~ubuntu-bionic` 这个版本的 Docker。你需要选择一个存在的版本进行安装。

例如，如果你想安装列表中的最新版本 `docker-ce/bionic 5:18.09.5~3-0~ubuntu-bionic`，你可以运行如下命令：

```bash
sudo apt-get install docker-ce=5:18.09.5~3-0~ubuntu-bionic docker-ce-cli=5:18.09.5~3-0~ubuntu-bionic containerd.io
```

请注意，由于你的 APT 源中没有 `docker-ce-cli=19.03.13~3-0~ubuntu-bionic` 这个版本，我也将其改为和 `docker-ce` 相同的版本。如果你的 APT 源中没有此版本的 `docker-ce-cli`，你可能需要使用 `apt-cache madison docker-ce-cli` 命令查看可用的版本，并选择一个合适的版本进行安装。

如果你必须安装 `docker-ce=19.03.13~3-0~ubuntu-bionic` 这个版本，你可能需要寻找包含此版本的其他 APT 源，或者从 Docker 的官方网站下载并手动安装。



如果你想要安装最新版本的 Docker，你可以使用下面的命令：

```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

这里没有指定 Docker 的版本，APT 将会默认选择最新版本进行安装。

然后，你可以使用下面的命令来验证 Docker 是否已经成功安装，以及查看其安装的版本：

```bash
docker --version
```

这个命令会显示 Docker 的版本信息，从而确认 Docker 是否已经成功安装，以及安装的是哪个版本。


从你的描述中看，命令`sudo apt-get install docker-ce docker-ce-cli containerd.io`在你的系统中没有任何反应。这可能是由以下原因造成的：
                  sudo apt-get install docker-ce docker-ce-cli containerd.io
1. 命令输入错误：你的命令中似乎少了一个 "s"，正确的命令应该是 `sudo apt-get install docker-ce docker-ce-cli containerd.io`。

2. 网络问题：如果你的网络连接有问题，APT 可能无法从源服务器下载包。

3. 源服务器问题：如果源服务器有问题，或者你的 APT 源列表（/etc/apt/sources.list）没有配置正确，APT 可能无法找到你想要的包。

4. 权限问题：如果你没有使用 `sudo`，那么你可能没有足够的权限来安装软件包。

首先，我建议你检查命令是否输入正确，然后再次尝试运行命令。如果问题仍然存在，你可能需要检查你的网络连接、APT 源列表，或者确认你是否有足够的权限来安装软件包。






$ 
sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \



 sudo add-apt-repository \
   "deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/ \
  $(lsb_release -cs) \
  stable"


  # gitlab-ce为稳定版本，后面不填写版本则默认pull最新latest版本





sudo docker pull registry.cn-hangzhou.aliyuncs.com/lab99/gitlab-ce-zh 


sudo docker run --detach --publish 8443:443 --publish 8090:80  --publish 8022:22  --name gitlab   --restart always --hostname 192.168.124.14  -v /data/software/gitlab/etc:/etc/gitlab -v /data/software/gitlab/logs:/var/log/gitlab  -v /data/software/gitlab/data:/var/opt/gitlab -v /etc/localtime:/etc/localtime:ro --privileged=true registry.cn-hangzhou.aliyuncs.com/lab99/gitlab-ce-zh