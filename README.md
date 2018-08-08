# findP3

近段刚刚上传了app新版本 ，上线前也是各种真机调试，包括公司一位同事的iOS9.2系统的iPhone6s , 一点问题都没有 可是两天后审核通过了 我们公司其他人下载app都非常流畅 ，也没有闪退的情况，唯独这个同事的iOS 9.2系统的iPhone6s 各种闪退 ， 集成的有友盟统计 看了崩溃原因根本无法定位 都是这种错误 这是在友盟统计上看到的

根本无法定位这问题
就在网上开始翻阅资料 最后找到了类似的问题，图片资源的问题
导致这种问题的原因是：在 Xcode 8 中，当你资源文件中[含有16位图]或者[图片显示模式γ值为'P3']且iOS targets设定为iOS 9.3以下就会出现这个问题. 如果你的app需要支持广色域显示的话，那你必须得把target设置成iOS 9.3+，相反，如果你的app不需要支持广色域且你想兼容 iOS 9.3 之前的项目，你就得把所有的16位的或者显示模式为'P3'图片全都替换成8位模式的SRGB颜色的图片
找到后，让UI再作图即可
 
把findP3.py 脚本和 ipa包都放在桌面上，然后再桌面执行 ./findP3.py 即可