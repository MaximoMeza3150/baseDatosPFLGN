import {listaEquipos} from './todosLosEquipos.js';

let listaDatalist = document.getElementById('lista-datalist');

for (let i = 0; i < listaEquipos.length; i++){
    let data = document.createElement('option')
    data.setAttribute('value',listaEquipos[i].nombre)
    listaDatalist.appendChild(data)
}

const inputTAG = document.getElementById('tag');
const pdf = document.getElementById('datasheet');

inputTAG.addEventListener('change', ()=> {
    for (let i = 0; i < listaEquipos.length; i++)
        if (inputTAG.value == listaEquipos[i].nombre){
            pdf.setAttribute('src', listaEquipos[i].enlace )
        }
})
