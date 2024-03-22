<script setup>
    import {ref,onMounted} from 'vue'

    const array = ref([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
    const items = array;
    const timeNow = ref();
    timeNow.value = 10
</script>

<template>
    <div class="taskbars">
        <a href="/controller ">Controller</a>
        <a href="/history ">Show history</a>
        <a href="/login ">Login</a>
    </div>

    <div class="context">
        <div class="giamsat">
            <div class="label1">
                <h2>Giám sát bơm</h2>
            </div>

            <div class ="boxTableGiamSat">
                <table>
                    <tr>
                        <td>ÁP SUÂT SETPOINT</td>
                    </tr>
                    <tr>
                        <td>ÁP SUAT DAU VÃO</td>
                    </tr>
                    <tr>
                        <td>ÁP SUAT DAU CUÔI</td>
                    </tr>
                    <tr>
                        <td>TAN SÓ CHAY BOM</td>
                    </tr>
                    <tr>
                        <td>TÂN SO MIN</td>
                    </tr>
                    <tr>
                        <td>TÂN SÓ MAX</td>
                    </tr>
                    <tr>
                        <td>THOI GIAN CHAY BOM</td>
                    </tr>
                    <tr>
                        <td>
                            H
                            M
                            S
                        </td>
                    </tr>
                    <tr>
                        <td>THÖI GIAN CHAY BOM TICH LÜY</td>
                    </tr>
                    <tr>
                        <td>                         
                            H
                            M
                            S
                        </td>
                    </tr>
                </table>
                <div class="label1">
                    <h2>Hệ số PID</h2>
                </div>

                <div>Кр</div>
                <div>Кi</div>
                <div>Кd</div>
            </div>
        </div>

        <div class="timeMonitor">
            <div class="label2">
                <h2>Dự đoán áp suất trong 24h tiếp theo</h2>
            </div>
            <div class ="boxTable">
                <table class="tableTime">
                    <tr>
                        <td :style="{ background: item == timeNow  ? 'red' : 'rgba(0, 0, 10, 1)' }"  
                            v-for="(item,index) in array.slice(0, 4)" :key="index" >
                        <div>
                            {{item}}
                            -
                            {{ item+1 }}
                            h
                        </div>
                        <div>
                            {{item}}
                            bar
                        </div>
                    </td>
                    </tr>
                    <tr>
                        <td :style="{ background: item == timeNow  ? 'red' : 'rgba(0, 0, 10, 1)' }"   
                            v-for="(item,index) in array.slice(4, 8)" :key="index" >
                            <div>
                                {{item}}h
                                -
                                {{ item+1 }}h
                            </div>
                            <div>
                                {{item}}
                                bar
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td :style="{ background: item == timeNow  ? 'red' : 'rgba(0, 0, 10, 1)' }"
                            v-for="(item,index) in array.slice(8, 12)" :key="index" >
                            <div>
                                {{item}}h
                                -
                                {{ item+1 }}h
                            </div>
                            <div>
                                {{item}}
                                bar
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td :style="{ background: item == timeNow  ? 'red' : 'rgba(0, 0, 10, 1)' }"
                            v-for="(item,index) in array.slice(12, 16)" :key="index" >
                            <div>
                                {{item}}h
                                -
                                {{ item+1 }}h
                            </div>
                            <div>
                                {{item}}
                                bar
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td :style="{ background: item == timeNow  ? 'red' : 'rgba(0, 0, 10, 1)' }"
                        v-for="(item,index) in array.slice(16, 20)" :key="index" >
                        <div>
                            {{item}}h
                            -
                            {{ item+1 }}h
                        </div>
                        <div>
                            {{item}}
                            bar
                        </div>
                    </td>
                    </tr>
                    <tr>
                        <td v-for="(item,index) in array.slice(20, 24)" :key="index"  
                            :style="{ background: item == timeNow  ? 'red' : 'rgba(0, 0, 10, 1)' }"
                            >
                            <div>
                                <div> 
                                    {{item}}h
                                    -
                                    {{ item+1 }}h
                                </div>
                                <div>
                                    {{item}}
                                    bar
                                </div>
                            </div>
                        </td>
                    </tr>
                </table>
            </div>
        </div>
    </div>

</template>
<style scoped>
    .taskbars{
        width: 150vh;
        height: 8vh;
        background-color: rgb(228, 132, 77);
        border-style: solid;
        border-width: 3px;
        border-color: red;
        display: flex;
        justify-content:center;
        
    }

    .taskbars a {
        margin: 0 50px;
        background-color: rgb(242, 242, 33);
        border-style: solid;
        border-width: 1px;
        border-color: rgb(119, 38, 219);
        border-radius: 10%;
        padding: 15px;
    }
    .context{
        width: 150vh;
        height: 90vh;
        background-color: sandybrown;
        display: flex;
    }
        .giamsat{
            width: 30%;
            height: 100%;
            background-color: yellow;
            border-style: solid;
            border-width: 3px;
            border-color: rgba(25, 1, 36, 0.933);
            margin-right: 10px;
        }
            .label1{
                height: 5%;
                margin-bottom: 10px;
                background-color: bisque;
                border-style: solid;
                border-color: black;
                border-width: 1px;
                margin: 1px;
                text-align: center;
            }
        .timeMonitor{
            width: 70%;
            height: 100%;
            background-color: aqua;
            border-style: solid;
            border-width: 3px;
            border-color: black;
            display: flex;
            flex-direction: column;
        }
            .label2{
                height: 5%;
                margin-bottom: 10px;
                background-color: bisque;
                border-style: solid;
                border-color: black;
                border-width: 1px;
                margin: 1px;
                text-align: center;
            }
            .boxTable{
                width: 100%;
                height: 100%;
                position: relative;
            }
                .tableTime{
                    width: 100%;
                    height: 100%;
                    position: relative;
                    text-align: center;
                }
                    .tableTime td {
                        border: 2px solid black;
                        color: rgb(75, 17, 234);
                    }

</style>