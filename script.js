function updateCategory(){
let u=document.getElementById("user_type").value;
let c=document.getElementById("category");
c.innerHTML="";
if(u=="Student"){c.innerHTML+="<option>Girls</option><option>Boys</option>";}
else if(u=="Teacher/Staff"){c.innerHTML+="<option>Staff</option>";}
else if(u=="Visitor"){c.innerHTML+="<option>Parents</option><option>Guest</option><option>Other</option>";}
}