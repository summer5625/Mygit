

// function addLi() {
//     var  newLi = document.createElement('li');
//     newLi.innerHTML = `<input type="checkbox">
//                        <p>
//                             <span>${$('title').value}</span>
//                             <input type="text">
//                        </p>
//                        <span>X</span>`;
//     $('backlog').insertBefore(newLi,$('backlog').children[0]);
// };


// $('btn').onclick = function () {
//     var getStr = $('title').value;
//     console.log(getStr);
//     addLi();
//     $('title').value = '';
//
// };

// function getOndoKey(str) {
//     var result = [];
//     var getLi = document.getElementById(str).getElementsByTagName('li');
//     console.log(getLi);
//     for (var i=0;i < getLi.length;i++){
//         var tex = getLi[i].children[1];
//         var textC = tex.getElementsByTagName('span');
//         console.log(textC);
//         result.push(textC.textContent);
//     };
//     console.log(result);
//     return result;
// }

// function storageData(strKey,listData) {
//     localStorage.removeItem(strKey);
//     localStorage.setItem(strKey, JSON.stringify(listData));
//
// }


// getOndoKey('backlog');

$(function () {

    //获取所有事项
    function getOnDo(str) {
        var result = [];
        var getLi = $(`#${str} li`);
        for (var i=0;i < getLi.length; i++){
            var getP = $(getLi[i]).children()[1];
            result.push($(getP).children()[0].textContent);
        }
        return result;
    }

    //保存信息
    function storageData(strKey,listData) {
        localStorage.removeItem(strKey);
        localStorage.setItem(strKey, JSON.stringify(listData));
    }

    //加载事务项
    function addNew(str,spanList) {
        for (var i=0;i < spanList.length;i++) {
             var  newLi = document.createElement('li');
             newLi.innerHTML = `<input type="checkbox">
                                <p>
                                    <span>${spanList[i]}</span>
                                    <input type="text">
                                </p>
                                <span>X</span>`;

             $(`#${str}`).prepend(newLi);
        }
    }

    //绑定待办事件到完成事件
    function toFinish() {
        var toDo = $('#backlog li');
        for (var i=0;i < toDo.length;i++){
            $(toDo[i].children[0]).click(function () {
                var dlet = $(this).parent('li').remove();
                $('#finishLog').prepend(dlet);
                var getList1 = getOnDo('backlog');
                var getList2 = getOnDo('finishLog');

                console.log(getList1,'toFinish');
                console.log(getList2,'toFinish');
                // storageData('backlog',getList1);
                // storageData('finishLog',getList2);

                var data1 = JSON.parse(localStorage.getItem('backlog'));
                var data2 = JSON.parse(localStorage.getItem('finishLog'));
                console.log(data1,'toFinish');
                console.log(data2,'toFinish');
            })
        }

    }

    //绑定完成事件到待办事件
    function toBacklog() {
        var finish = $('#finishLog li');
        for (var i=0;i < finish.length;i++){
            $(finish[i].children[0]).click(function () {
                var delt = $(this).parent('li').remove();
                $('#backlog').append(delt);
                var getList1 = getOnDo('backlog');
                var getList2 = getOnDo('finishLog');
                console.log(getList1,'toBacklog');
                console.log(getList2,'toBacklog');
                // storageData('backlog',getList1);
                // storageData('finishLog',getList2);

                var data1 = JSON.parse(localStorage.getItem('backlog'));
                var data2 = JSON.parse(localStorage.getItem('finishLog'));
                console.log(data1,'toBacklog');
                console.log(data2,'toBacklog');
            })
        }
    }



    //localStorage.clear();
    //toFinish();
    //toBacklog();


    // var data1 = JSON.parse(localStorage.getItem('backlog'));
    // var data2 = JSON.parse(localStorage.getItem('finishLog'));
    // console.log(data1);
    // console.log(data2);

});














