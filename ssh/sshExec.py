import paramiko
import time
def chanel_exe_cmd(ChanelSSHOb,cmd,t=0.1):
    ChanelSSHOb.send(cmd)
    ChanelSSHOb.send("\n")
    time.sleep(t)
    resp = ChanelSSHOb.recv(9999).decode("utf8")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("Exec sshCmd: %s" % (cmd))
    print("--------------------")
    print("Exec Result: %s" % (resp))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    return resp
    
def creatSShConnectOb(ip_remote, port_remote, username, password):
    print('---------- start to create SSH object')
    print('Remote SSH Info:\n\'ip:%s  port:%d  username:%s  password:%s\'\n' %(ip_remote, port_remote, username, password))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip_remote, port_remote, username=username, password=password, timeout=60) #  timeout protection
        return ssh
    except:
        print('Warning:\nFist connect the ABC failed, now will retry!')
        ssh.connect(ip_remote, port_remote, username=username, password=password, timeout=60) #  timeout re-try
        print('Error:\nAttempt to connect ABC failed!!! Please check the IP / port/ account / password.')
    else:
        print('Info:\nConnect remote ABC success.')

def sftp_upload_file(host,user,password,server_path, local_path,timeout=10):
    """
    上传文件，注意：不支持文件夹
    :param host: 主机名
    :param user: 用户名
    :param password: 密码
    :param server_path: 远程路径，比如：/home/sdn/tmp.txt
    :param local_path: 本地路径，比如：D:/text.txt
    :param timeout: 超时时间(默认)，必须是int类型
    :return: bool
    """
    try:
        t = paramiko.Transport((host, 22))
        t.banner_timeout = timeout
        t.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local_path, server_path)
        t.close()
        return True
    except Exception as e:
        print(e)
        return False

def sftp_down_file(host,user,password,server_path, local_path,timeout=10):
    """
    下载文件，注意：不支持文件夹
    :param host: 主机名
    :param user: 用户名
    :param password: 密码
    :param server_path: 远程路径，比如：/home/sdn/tmp.txt
    :param local_path: 本地路径，比如：D:/text.txt
    :param timeout: 超时时间(默认)，必须是int类型
    :return: bool
    """
    try:
        t = paramiko.Transport((host,22))
        t.banner_timeout = timeout
        t.connect(username=user,password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(server_path, local_path)
        t.close()
        return True
    except Exception as e:
        print(e)
        return False