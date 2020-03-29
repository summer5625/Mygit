var name = 'liu';
function hello() {
    alert('hello2 '+name);
};

(function () {
    var name = 'liu';
    var hello = function () {
    alert('hello4 '+name);
    };
    window.sss = hello;
})();