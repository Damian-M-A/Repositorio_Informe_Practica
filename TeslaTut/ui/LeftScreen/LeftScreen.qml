import QtQuick 

Rectangle{
    id:leftScreen
    anchors{
        left: parent.left
        right: rightScreen.left
        bottom: bottonBar.top
        top: parent.top
    }
    color:"white"

    Image{
        id: carRender
        anchors.centerIn: parent
        width: parent.width * 0.75
        height: parent.height * 0.75
        fillMode: Image.PreserveAspectFit
        source: "qrc:/ui/assets/car.jpg"
    }
}
