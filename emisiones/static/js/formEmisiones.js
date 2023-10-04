let $sites = document.getElementById('selectorSite')
let $yacimiento = document.getElementById('selectorYacimiento')
let $area = document.getElementById('selectorArea')
let $sistema = document.getElementById('selectorSistemas')


let sites = ['Malvinas', 'Pisco']
let yacimientos = ['Procesos', 'Servicios Auxiliares']
let areas = ['Procesos 1', 'Procesos 2', 'Procesos 3', 'Servicios Auxiliares 1', 'Servicios Auxiliares 2']
let SSAA1 = ['Turbogeneración', 'Bombas contraincendio']
let SSAA2 = ['Sistema de almacenamiento y bombeo de NGL', 'Sistema de gas combustible', 'Sistema de recuperación de vapores', 'Sistema de drenaje abierto', 'Sistema de drenaje cerrado', 'Sistema de drenaje frío cerrado', 'Sistema de flare de alta presión', 'Sistema de flare de baja presión']


function mostrarLugares(arreglo, lugar){
    let elementos = '<option selected disables>-</option>'
    for(let i = 0; i < arreglo.length; i++) {
        elementos += '<option value="' + arreglo[i] +'">' + arreglo[i] +'</option>'
    }
    lugar.innerHTML = elementos
}

mostrarLugares(sites,$sites)

$sites.addEventListener('change', function(){
    let valor = $sites.value 
    switch(valor){
        case 'Malvinas':
            break
        case 'Pisco':
            let recortar0 = yacimientos.slice(0,2)
            mostrarLugares(recortar0,$yacimiento)
            break
    }
})
$yacimiento.addEventListener('change', function(){
    let valor = $yacimiento.value 
    switch (valor) {
        case 'Procesos':
            let recortar0 = areas.slice(0,3)
            mostrarLugares(recortar0,$area)            
            break;
        case 'Servicios Auxiliares':
            let recortar1 = areas.slice(3,5)
            mostrarLugares(recortar1,$area)   
        break;
    }
})
$area.addEventListener('change', function(){
    let valor = $area.value
    switch (valor) {
        case 'Servicios Auxiliares 1':
            mostrarLugares(SSAA1,$sistema)
            break;
        case 'Servicios Auxiliares 2':
            mostrarLugares(SSAA2,$sistema)
            break;
    }
})