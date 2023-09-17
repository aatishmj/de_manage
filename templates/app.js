var form= document.getElementById("myform"),
imgInput=document.querySelector(".img"),
file=document.getElementById("imgInput"),
name =document.getElementById("name"),
post=document.getElementById("post"),
phone=document.getElementById("number"),
sDate=document.getElementById("sDate"),
submitBtn=document.querySelector("Submit"),
userinfo=document.getElementById("data")

let getDat= localStorage.getItem('userProfile') ? JSON.parse(localStorage.getItem("userProfile")): []
let isData =false,editId
file.onchange=function(){
    if(file.files[0].size<10000000){
        var fileReader=new fileReader();
        fileReader.onload=function(e){
            imgUrl=e.target.result
            imgInput.src-imgUrl
        }
        fileReader.readAsDataURL(file.files[0])
    }
    else{
        alert("This File is too large!")
    }
}