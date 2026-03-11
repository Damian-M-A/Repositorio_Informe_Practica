import QtQuick

Item {
    property var hvacController
    Rectangle {
        id: decrementButton
        anchors {
            left: parent.left
            top: parent.top
            bottom: parent.bottom
        }
        width: height / 2
        color: "black"

        Text {
            id: decrementText
            anchors.centerIn: parent
            text: "<"
            color: "white"
            font.pixelSize: 35
        }
        MouseArea{
            anchors.fill: parent
            onClicked: hvacController.decrementTemp()

        }

        Text {
            id: targetTempText
            anchors {
                left: decrementText.right
                leftMargin: 15
                verticalCenter: parent.verticalCenter
            }
            text: hvacController.targetTemp

            color: "white"
            font.pixelSize: 40
        }

        Rectangle {
            id: incrementButton
            anchors {
                left: targetTempText.right
                leftMargin: 15
                top: parent.top
                bottom: parent.bottom
            }
            width: height / 2
            color: "black"

            Text {
                id: incrementText
                anchors.centerIn: parent
                text: ">"
                color: "white"
                font.pixelSize: 35
            }
            MouseArea{
                anchors.fill: parent
                onClicked: hvacController.incrementTemp()

            }
        }
    }
}

