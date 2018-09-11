/**
 * Created by hezz on 2018/8/30.
 */
$(function () {
    //1.初始化Table
    var oTable = new TableInit();
    oTable.Init();

    //2.初始化Button的点击事件
    var oButtonInit = new ButtonInit();
    oButtonInit.Init();

    /*    alert('iii');
     $("#btn_edit").click(function () {
     alert("hello1");
     $.ajax({
     type: "POST",
     url: "/aaa/",
     data: {name: c},
     dataType: "json",
     success: function (data) {
     $("#p").text(data.msg + data.code)
     }
     });
     });*/
});

function editBook(id) {
    $.ajax({
        type: "POST",
        url: "get_book_detail",
        // url: "/home/get_book_detail",
        data: {
            'id': id
        },
        dataType: "json",
        success: function (data) {
            // $("#p").text(data.msg + data.code)
            if (1 == data.code) {
                $("#book_name_text").val(data.data['name']);
                $("#author_text").val(data.data['authors']);
                $("#count_text").val(data.data['chapter_count']);
                $("#book_id_text").val(data.data['id']);
                $('#modal-container-add').modal();
            } else {
                toastr.warning(data.msg);
            }
            // $("#tb_books").bootstrapTable('refresh');
        }
    });
}

function deleteBook(id) {
    if (id == null || id == '' || id == "")
        return;

    $.ajax({
        type: "POST",
        url: "delete_book",
        // url: "/home/delete_book",
        data: {
            'id': id
        },
        dataType: "json",
        success: function (data) {
            if (1 == data.code) {
                toastr.success('删除成功!');
            } else {
                toastr.warning(data.msg);
            }
            $("#tb_books").bootstrapTable('refresh');
        }
    });
}

function objToStr(obj) {
    str = "";
    for (var i in obj) {
        str += obj[i];
    }
    return str;
}

var TableInit = function () {
    var oTableInit = new Object();
    //初始化Table
    oTableInit.Init = function () {
        $('#tb_books').bootstrapTable({
            url: 'get_book_list',         //请求后台的URL（*）
            // url: '/home/get_book_list',         //请求后台的URL（*）
            method: 'post',                      //请求方式（*）
            // data:"data",                         //取的数据字段名
            contentType: "application/x-www-form-urlencoded; charset=UTF-8", // 默认是：'application/json'， 不改的话，后台获取不到数据！ ###### 非常重要！！######
            toolbar: '#toolbar',                //工具按钮用哪个容器
            striped: true,                      //是否显示行间隔色
            cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
            pagination: true,                   //是否显示分页（*）
            sortable: false,                     //是否启用排序
            sortOrder: "asc",                   //排序方式
            queryParams: oTableInit.queryParams,//传递参数（*）
            sidePagination: "server",           //分页方式：client客户端分页，server服务端分页（*）
            pageNumber: 1,                       //初始化加载第一页，默认第一页
            pageSize: 10,                       //每页的记录行数（*）
            pageList: [10, 25, 50, 100],        //可供选择的每页的行数（*）
            search: false,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
            strictSearch: true,
            showColumns: true,                  //是否显示所有的列
            showRefresh: true,                  //是否显示刷新按钮
            minimumCountColumns: 2,             //最少允许的列数
            clickToSelect: true,                //是否启用点击选中行
            height: 500,                        //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
            uniqueId: "id",                     //每一行的唯一标识，一般为主键列
            showToggle: true,                    //是否显示详细视图和列表视图的切换按钮
            cardView: false,                    //是否显示详细视图
            detailView: false,                   //是否显示父子表
            columns: [{
                checkbox: true
            }, {
                field: 'name',
                title: '书名',
                valign: 'middle',
                align: 'left',
                halign: 'center'
            }, {
                field: 'create_time',
                title: '创建日期',
                valign: 'middle',
                align: 'left',
                halign: 'center'
            }, {
                field: 'authors',
                title: '作者',
                valign: 'middle',
                align: 'left',
                halign: 'center'
            }, {
                field: 'chapter_count',
                title: '章节数',
                valign: 'middle',
                align: 'left',
                halign: 'center'
            }, {
                field: 'options',
                title: '操作',
                valign: 'middle',
                align: 'left',
                halign: 'center',
                formatter: function (value, row, index) {
                    var e1 = '<a   onclick="editBook( \'' + row.id + '\')">编辑</a> ';
                    var e2 = '<a   onclick="deleteBook( \'' + row.id + '\')">删除</a> ';
                    return [e1, e2].join('');
                }
            },]
        });
    };


    //得到查询的参数
    oTableInit.queryParams = function (params) {
        var temp = {   //这里的键的名字和控制器的变量名必须一直，这边改动，控制器也需要改成一样的
            limit: params.limit,   //页面大小
            offset: params.offset,  //页码
            order: params.order,// 排序方式
            ordername: params.sort,//排序字段
            bookname: $("#txt_search_book_name").val(),
            author: $("#txt_search_statu").val(),
            starttime:$("#search_start_time").val(),
            endtime:$("#search_end_time").val(),
        };
        return temp;
    };
    return oTableInit;
};


var ButtonInit = function () {
    var oInit = new Object();
    var postdata = {};

    oInit.Init = function () {
        $("#btn_save_book").click(function () {

            book_name = $("#book_name_text").val();
            authors = $("#author_text").val();
            chapter_count = $("#count_text").val();
            id = $("#book_id_text").val();
            $.ajax({
                type: "POST",
                url: "save_book",
                // url: "/home/save_book",
                data: {
                    'name': book_name,
                    'authors': authors,
                    'chapter_count': chapter_count,
                    'id': id
                },
                dataType: "json",
                success: function (data) {
                    // $("#p").text(data.msg + data.code)
                    if (1 == data.code) {
                        toastr.success(data.msg);
                    } else {
                        toastr.warning(data.msg);
                    }
                    $("#tb_books").bootstrapTable('refresh');
                }
            });
        });

        $("#btn_edit").click(function () {
            var arrselections = $("#tb_books").bootstrapTable('getSelections');
            if (arrselections.length > 1) {
                toastr.warning('只能选择一行进行编辑');
                return;
            }
            if (arrselections.length <= 0) {
                toastr.warning('请选择有效数据');
                return;
            }
            editBook(arrselections[0]['id']);
        });

        $("#btn_delete").click(function () {
            var arrselections = $("#tb_books").bootstrapTable('getSelections');
            if (arrselections.length <= 0) {
                toastr.warning('请选择有效数据！');
                return;
            }
            Ewin.confirm({message: "确认要删除选择的数据吗？"}).on(function (e) {
                if (!e) {
                    return;
                }
                // var args = JSON.stringify(arrselections);
                // alert(args);
                var ids = [];
                for (var i = 0; i < arrselections.length; i++) {
                    ids.push(arrselections[i]['id']);
                }
                $.ajax({
                    type: "post",
                    url: "batch_delete_book",
                    // url: "/home/batch_delete_book",
                    data: {"ids": ids},
                    dataType: "json",
                    success: function (data) {
                        if (1 == data.code) {
                            toastr.success(data.msg);
                        } else {
                            toastr.warning(data.msg);
                        }
                        $("#tb_books").bootstrapTable('refresh');
                    },
                    error: function () {
                        toastr.error('Error');
                        //清除当前的列表  toastr.clear()
                    }
                    // complete: function () {
                    //
                    // }

                });
            });
        });

        $("#btn_query").click(function () {
            $("#tb_books").bootstrapTable('refresh');
        });
    };

    return oInit;
};


/*yyyy-mm-dd
yyyy-mm-dd hh:ii
yyyy-mm-ddThh:ii
yyyy-mm-dd hh:ii:ss
yyyy-mm-ddThh:ii:ssZ
日期格式， p, P, h, hh, i, ii, s, ss, d, dd, m, mm, M, MM, yy, yyyy 的任意组合。*/
var time_format = "yyyy-mm-dd"

$("#search_start_time").datetimepicker({//选择年月日
　　　　　　format: time_format,
　　　　　　language: 'zh-CN',
　　　　　　weekStart: 1,
　　　　　　todayBtn: 1,//显示‘今日’按钮
　　　　　　autoclose: 1,
　　　　　　todayHighlight: 1,
　　　　　　startView: 2,
　　　　　　minView: 2,  //Number, String. 默认值：0, 'hour'，日期时间选择器所能够提供的最精确的时间选择视图。
　　　　　　clearBtn:true,//清除按钮
　　　　　　forceParse: 0
});
$("#search_end_time").datetimepicker({//选择年月日
　　　　　　format: time_format,
　　　　　　language: 'zh-CN',
　　　　　　weekStart: 1,
　　　　　　todayBtn: 1,//显示‘今日’按钮
　　　　　　autoclose: 1,
　　　　　　todayHighlight: 1,
　　　　　　startView: 2,
　　　　　　minView: 2,  //Number, String. 默认值：0, 'hour'，日期时间选择器所能够提供的最精确的时间选择视图。
　　　　　　clearBtn:true,//清除按钮
　　　　　　forceParse: 0
});

/*
$('.form_datetime').datetimepicker({
        language: 'zh-CN',
        weekStart: 1,
        todayBtn:  1,
		autoclose: 1,
		todayHighlight: 1,
		startView: 2,
		forceParse: 0,
        showMeridian: 1
    });*/
