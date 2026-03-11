import QtQuick 
import QtQuick.Window 
import "ui/BottomBar" as Components
import "ui/RightScreen" as Components
import "ui/LeftScreen" as Components

Window {
    width: 1024
    height: 600
    visible: true
    title: qsTr("Tesla Tutorial QML")

    Components.LeftScreen{
        id: leftScreen
    }
    Components.RightScreen{
        id: rightScreen
    }
    Components.BottomBar{
        id: bottonBar
    }

}
