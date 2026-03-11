import QtLocation 6.10
import QtPositioning
import QtQuick

Rectangle {
    id: rightScreen
    anchors {

        top: parent.top
        bottom: bottonBar.top
        right: parent.right
    }
    color: "orange"
    width: parent.width * 2 / 3

    Plugin {
        id: mapPlugin
        name: "osm"

    }
    Map {
        anchors.fill: parent
        plugin: mapPlugin
        center: QtPositioning.coordinate(-33.30353, -70.74209)
        zoomLevel: 20

        // MapQuickItem{
        //     coordinate: QtPositioning.coordinate(-33.30353, -70.74209)
        //     anchorPoint.x: icon.width / 2
        //     anchorPoint.y: icon.height
        //     sourceItem: Image {
        //         id: icon
        //         source: "qrc:/ui/assets/car.jpg"
        //         width: 64
        //         height: 64
        //     }

        // }

    }
    Image {
        id: lockIcon
        anchors {
            left: parent.left
            top: parent.top
            margins: 20
        }
        width: parent.width / 40
        fillMode: Image.PreserveAspectFit
        source: (system.carLocked ? "qrc:/ui/assets/open.png" : "qrc:/ui/assets/lock.png")
    }
    MouseArea {
        anchors.fill: parent
        onClicked: system.setCarLocked(!system.carLocked)
        }

    Text {
        id: dateTimeDisplay
        anchors {
            left: lockIcon.right
            leftMargin: 40
            bottom: lockIcon.bottom
        }
        font.pixelSize: 12
        font.bold: true
        color: "black"
        text: system.currentTime
        }
    Text {
        id: outdoorTemp
        anchors {
            left: dateTimeDisplay.right
            leftMargin: 40
            bottom: dateTimeDisplay.bottom
        }
        font.pixelSize: 12
        font.bold: true
        color: "black"
        text: system.outTemp + "°C"
    }
    Text {
        id: userName
        anchors {
            left: outdoorTemp.right
            leftMargin: 40
            bottom: outdoorTemp.bottom
        }
        font.pixelSize: 12
        font.bold: true
        color: "black"
        text: system.userName
    }
    NavigationSearchBox{
        id: navSearchBox
        width: parent.width * 1/3
        height: parent.height * 1/12

        anchors{
            left: lockIcon.left
            top: lockIcon.bottom
            topMargin: 15
        }
    }
}
