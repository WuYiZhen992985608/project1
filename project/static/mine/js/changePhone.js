$(document).ready(function() {
    var account = document.getElementById('account')
    var accounterr = document.getElementById('accounterr')
    var checkerr = document.getElementById('checkerr')
    account.addEventListener('focus', function () {
        accounterr.style.display = 'none'
        checkerr.style.display = 'none'
    }, false)
    account.addEventListener('blur', function () {
        var inputStr = this.value
        if (inputStr.length < 8 || inputStr.length > 12) {
            accounterr.style.display = 'block'
            return
        }
        $.post('/checkuserid/1/', {'userid': inputStr}, function (data) {
            if (data.status == 'error') {
                checkerr.style.display = 'block'
            }
        })
    })

})