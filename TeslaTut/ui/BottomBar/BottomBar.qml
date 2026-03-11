import QtQuick


Rectangle{
        id: bottonBar
        anchors {
            left: parent.left
            right: parent.right
            bottom: parent.bottom
        }
        color: "black"
        height: parent.height / 12

    Image{
        id: carSettingsIcon
        anchors{
            left: parent.left
            leftMargin: 30
            verticalCenter: parent.verticalCenter
        }
        height: parent.height * 0.85
        fillMode: Image.PreserveAspectFit
        source: "qrc:/ui/assets/electric-car.png"
    }
    HVAC{
        id:driverHAControl
        anchors{
            top: parent.top
            bottom: parent.bottom
            left: carSettingsIcon.right
            leftMargin: 100
        }
        hvacController: hvadriver
    }
    HVAC{
        id:passangerHAControl
        anchors{
            top: parent.top
            bottom: parent.bottom
            right: parent.right
            rightMargin: 200
        }
        hvacController: hvapass
    }
}
