#!/bin/bash
current_dir=`pwd`
# 初始化sFlow参数变量
app_name="ddos_simulation_app.py"
# 遍历所有参数
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        --app_name)
            app_name="$2"
            shift # past argument
            ;;
        *)
            # 如果不认识的参数，可以处理错误或者忽略
            echo "Unknown option: $1"
            ;;
    esac
    shift # past argument or value
done

#启动ryu控制器
start_ryu_with_app() {
    app_file_path=$current_dir/../network/ryu-app/$app_name 
    #find ryu-manager
    type ryu-manager >/dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "ryu-manager is not found or has an error. "
        return 1
    else
        if [ -f $app_file_path]; then
            ryu-manager $app_file_path
            return 0
        else
            echo "can no find ryu app!:" "$app_file_path"
            return 1
        fi
    fi
    
}

# 调用start_sflow函数并检查返回值
if start_ryu_with_app; then
    echo 'ryu app did not start!'
    exit 1 
fi



