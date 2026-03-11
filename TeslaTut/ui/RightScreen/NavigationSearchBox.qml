import QtQuick

Rectangle{
    id: navSearchBox
    radius: 5
    color: "#EDE9E8"

    Image{
        id:searchIcon
        anchors{
            left: parent.left
            leftMargin: 25
            verticalCenter: parent.verticalCenter

        }
        height: parent.height * .45
        fillMode: Image.PreserveAspectFit
        source: "qrc:/ui/assets/search.png"

    }
    //label
    Text{
        id:navPlaceHolderText
        visible: navTextInput.text === ""
        color:"#373737"
        text: "navigate"
        anchors{
            verticalCenter: parent.verticalCenter
            left: searchIcon.right
            leftMargin: 20
        }
    }
    //textarea
    TextInput{
        id:navTextInput
        // esto evita el desbordamiento del texto en el padre
        clip:true
        anchors{
            top: parent.top
            bottom: parent.bottom
            right: parent.right
            left: searchIcon.right
            leftMargin: 20
        }
        verticalAlignment: Text.AlignVCenter
        font.pixelSize: 16
    }

}
