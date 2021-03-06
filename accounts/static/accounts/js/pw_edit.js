// Regex 통과 여부 판단을 위한 tool function
function regexCheck(regex, what, message) {
    if(regex.test(what.value)) {
      return true;
    };
    alert(message);
    what.value = "";
    what.focus();
};
  
// 공백 여부 판단을 위한 tool function
function blankCheck(field, message) {
    if(field.vaule == "") {
      alert(message);
      field.focus();
    };
};

function validateForm(data) {
    const $this = data;
    const csrfmiddlewaretoken = $this.dataset.csrfmiddlewaretoken;

    // input 변수 지정
    var pwInput = document.getElementById("pw");
    var pw1Input = document.getElementById("pw1");
    var pw2Input = document.getElementById("pw2");

    // 영문, 숫자, 특수문자 최소 한 글자씩 포함 & 8자 이상
    var pwRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[~$@^$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$/;
      
    if(blankCheck(pwInput, "현재 비밀번호를 입력해주세요.")) {
      return false;
    };

    $.ajax({
      type: 'POST',
      url: "/accounts/passwordcheck/",
      data: {
        'csrfmiddlewaretoken': csrfmiddlewaretoken,
        'origin_password' : pwInput.value
      },
      datatype: 'json',
      success: function (data) {
        console.log(data)
        if (data['pwcheck'] == "false") {
          alert("현재 비밀번호를 확인해 주세요!");
          pwInput.focus();
          return false;
        } else {
          return true;
        }
      }
    })

    if(blankCheck(pw1Input, "새로운 비밀번호를 입력해주세요.")) {
        return false;
      };

    if(blankCheck(pw2Input, "새로운 비밀번호를 입력해주세요.")) {
      return false;
    };

    if (!regexCheck(pwRegex, pw1Input, "영문, 숫자, 특수문자(~@^$!%*#?&)를 최소 한글자씩 포함한 8자 이상의 비밀번호를 입력해주세요.")) {
      return false;
    };
     
    if (pw1Input.value != pw2Input.value) {
        alert("비밀번호가 일치하지 않습니다.");
        pw1Input.focus();
        return false;
    };


    
    // 모든 유효성 검사 통과 시 form 제출
    document.getElementById("submit").submit();
  };

// information
var infoPw = document.getElementById("alert-pw");

infoPw.addEventListener("click", () => {
  alert("영문, 숫자, 특수문자(~@^$!%*#?&)를 최소 한글자씩 포함한 8자 이상의 비밀번호를 입력해주세요.") 
});