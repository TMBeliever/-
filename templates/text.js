new Vue({
    el:'#app',
    data:{first:!0,loading:!1,tableData:null,ruleForm:{username:'',password:''},
        rules:{username:[{required:!0,message:'\u8BF7\u8F93\u5165\u5B66\u53F7',trigger:'blur'},
            {len:10,message:'\u5B66\u53F7\u957F\u5EA6\u4E3A10\u4E2A\u6570\u5B57',trigger:'blur'}],
            password:[{required:!0,message:'\u8BF7\u8F93\u5165\u5BC6\u7801',trigger:'blur'}]}},
    methods:{
        tableRowClassName:function tableRowClassName(a){return 60>a.score||'\u4E0D\u53CA\u683C'===a.score?'el-tag--danger':''},
        submitForm:function submitForm(a){var b=this;this.$refs[a].validate(function(c){
    return void function () {
            var d = b, e = new FormData;
            e.append('username', b.ruleForm.username), e.append('password', b.ruleForm.password), b.loading = !0, axios.post('/text/', e).then(function (f) {
                console.log(f)
                1 === f.data.code && (d.tableData = f.data, d.first = !1), d.loading = !1, d.$message({
                    showClose: !0,
                    message: f.data.msg,
                    type: 1 === f.data.code ? 'success' : 'error'
                })
            }).catch(function (f) {
                d.loading = !1, console.log(f), d.$message({
                    showClose: !0,
                    message: '\u7F51\u7EDC\u8FDE\u63A5\u5F02\u5E38',
                    type: 'error'
                })
            })
        }() && !!c
})}}});