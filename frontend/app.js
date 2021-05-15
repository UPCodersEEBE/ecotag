var opts = {
    method: "GET",    
} 

async function getInfo(){
    const response = await fetch(
        'https://ecotag.herokuapp.com/object_info/97935cab-46c0-46e6-a255-5bde9bd0b82a',
        opts
    )       
    const data = await response.json();
    const objName = data.description;
    const impact = data.impact;
    console.log(impact);
    const h2o = impact.H2O;
    const co2 = impact.CO2;
    const e = impact.E;
    console.log(h2o);
    console.log(co2);
    console.log(e);
    document.getElementById("myText").innerHTML = objName;
    document.getElementById("co2").innerHTML = co2;
    document.getElementById("h2o").innerHTML = h2o;
    document.getElementById("e").innerHTML = e;
}
getInfo();
