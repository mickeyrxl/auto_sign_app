# auto_sign_app 

### sign in an app automatically using python

* ### First you have to install adb & weditor in your PC, and uiautomator2 should be installed in your device.
> Here is the guideline of uiautomator2 -> https://github.com/openatx/uiautomator2/blob/master/README.md

* ### This command  $adb devices will list all devices attached. So that youu can get the device's serial code.

* ### Init the device by this. $python -m uiautomator2 init

* ### Open the browser to connect device by $python -m weditor
> You can also create a shortcut on your desktop $python -m weditor --shortcut

* ### Input the ip or serial code of device in the browser, and then click the connect button.
