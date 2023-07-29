 const abc= document.getElementById("txtBox2").value;

function f1(e) {
    let value = e.value;
    document.getElementById("txtBox2").style.fontSize = value + "px";
}

function f2(e) {
    // document.getElementById("txtBox2").style.fontWeight="bold"
    if (document.getElementById("txtBox2").style.fontWeight == "bold") {
        document.getElementById("txtBox2").style.fontWeight = "normal";
        e.classList.remove("active");
    }
    else {
        document.getElementById("txtBox2").style.fontWeight = "bold";
        e.classList.add("active");
    }
}

function f3(e) {
    if (document.getElementById("txtBox2").style.fontStyle == "italic") {
        document.getElementById("txtBox2").style.fontStyle = "normal";
        e.classList.remove("active");
    }
    else {
        document.getElementById("txtBox2").style.fontStyle = "italic";
        e.classList.add("active");
    }
}

function f4(e) {
    if (document.getElementById("txtBox2").style.textDecoration == "underline") {
        document.getElementById("txtBox2").style.textDecoration = "none";
        e.classList.remove("active");
    }
    else {
        document.getElementById("txtBox2").style.textDecoration = "underline";
        e.classList.add("active");
    }
}

function f5(e) {
    document.getElementById("txtBox2").style.textAlign = "left";
}

function f6(e) {
    document.getElementById("txtBox2").style.textAlign = "center";
}

function f7(e) {
    document.getElementById("txtBox2").style.textAlign = "right";
}

function f8(e) {
    if (document.getElementById("txtBox2").style.textTransform == "uppercase") {
        document.getElementById("txtBox2").style.textTransform = "none";
        e.classList.remove("active");
    }
    else {
        document.getElementById("txtBox2").style.textTransform = "uppercase";
        e.classList.add("active");
    }
}

function f9() {
    document.getElementById("txtBox2").style.fontWeight = "normal";
    document.getElementById("txtBox2").style.textAlign = "left";
    document.getElementById("txtBox2").style.fontStyle = "normal";
    document.getElementById("txtBox2").style.textTransform = "capitalize";
    document.getElementById("txtBox2").value = "";
}

function f10(e) {
    let value = e.value;
    document.getElementById("txtBox2").style.color = value;
}

 window.addEventListener('load', () => {
     document.getElementById("txtBox2").value = "";
 });