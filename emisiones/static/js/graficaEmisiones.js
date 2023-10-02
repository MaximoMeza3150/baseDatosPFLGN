const getOptionChart = async () => {
    try {
        const response = await fetch("")
        
    } catch (ex) {
        alert(ex)
    }
}

const initChart = async() => {
    const mychart = echarts.init(document.getElementById('chart'))
}

window.addEventListener('load', async()=>{
    await initChart();
})