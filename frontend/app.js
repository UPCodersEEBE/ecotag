
/*fetch('https://ecotag.herokuapp.com/object_info/')
    .then(res => res.json())
    .then((out) => {
        console.log('Output: ', out);
}).catch(err => console.error(err));
*/
var opts = {
    method: "GET",
    mode: "no-cors"
} 



async function getInfo(){
    const response = await fetch(
        'https://ecotag.herokuapp.com/object_info/97935cab-46c0-46e6-a255-5bde9bd0b82a',
        opts
    )       
    const data = response.json();
    const impact = data.impact;
    console.log(impact)
}
getInfo();
