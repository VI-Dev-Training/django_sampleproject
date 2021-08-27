
let loginBtn = document.getElementById('login-btn');
let logoutBtn = document.getElementById('logout-btn');


let token = localStorage.getItem('token')

if (token){
    loginBtn.remove()
} else {
    logoutBtn.remove()
}

logoutBtn.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location = 'file:///home/adithya/Desktop/Front-End/login.html'
})

projectsUrl = 'http://127.0.0.1:8000/api/projects/'

let getProjects = () => {

    fetch(projectsUrl)
    .then(response => response.json())
    .then(data => {
        showProjects(data)
    })
}


let showProjects = (projects) => {

    let projectsWrapper = document.getElementById("projects-wrapper");

    for( let project of projects) {
        
        let projectTitle = `  
        <div> 
            <p> ${project.title} </p>         
        </div>
        `

        projectsWrapper.innerHTML += projectTitle;
    }

}

getProjects()