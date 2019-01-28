def fn_outter():
    print("fn_outter被调用")
    def fn_inner():
        print("fn_inner被调用")
    fn_inner()#调用一次
    fn_inner()#调用2次
    print("fn_outter调用结束")
fn_outter()