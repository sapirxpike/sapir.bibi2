console.log("im inside fetch example")

function getusers(){
    console.log('clicked');
    fetch(input:'https://reqres.in/api/users?page=2').then(
        response => response.json()
    ).then(
        response.obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data){}
    //console.log(response_obj_data);
    const curr_main = document.querySelector(selectors: "main");
    for(let user of response_obj_data) {
        const section = document.createElement(tagname: 'section');
        section.innerHTML = ``
        <img src="${user.avatar}" alt="Profile Picture"/>
        <div>
            <span>${user.first_name} ${user.last_name}</span>
            <br>
            <a href="mailto:${user.email}">Send Email</a>
           </div>
        ;
        curr_main.appendChild(section);
    }
}