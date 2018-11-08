options = new Object();

function openSelector() {
        document.getElementById("myForm").style.display = "block";
}

function closeSelector() {
        document.getElementById("myForm").style.display = "none";
}

formData = new Array();
q = new Array();

addElement = function( count, que, res ) {
        var element = angular.element("<div id="+count+"  class=form-element >"+"</div>");
        var target = document.getElementById('preview');
        angular.element(target).append(element);

        $("#"+count).append("<h1>"+que+"</h1>");
        q[count-1] = que;
        if(res=="Text"){
                $("#"+count).append("<input type=\"text\" ng-model=\"e.q"+count+"\"/>");
        }
        if(res=="Radio"){
                var optlen = options.length;
                for (var i = 0; i < optlen; i++) {
                    $("#"+count).append("<input type=radio>"+options[i]+"</h1><br />");
                }
        }
}

var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
        $scope.count=0;
        $scope.load = function() {
                console.log("Loading Form Template");

                $.getJSON('sample-data/formtemplate.json',function(data){
                        //console.log(data);
                        $.each(data, function(key,val){
                                //console.log(key);
                                //console.log(val[0].type);

                                $scope.count++;
                                if(Object.keys(val).length==2)
                                {
                                        options = val[1].values;
                                }
                                //console.log(options);
                                addElement($scope.count,key,val[0].type);
                        });
                });
        }
        $scope.create = function() {
                $scope.count++;
                addElement($scope.count,$scope.elem.que,$scope.elem.res);
                formData[$scope.count] =  JSON.stringify($scope.elem);
                console.log(formData);
        };
        $scope.newElement = function() {
                console.log("Handled");
                console.log($scope.elem);
                closeSelector();
                $scope.create();
        };
        $scope.checkMultiple = function() {
                if ($scope.elem.re  == "undefined")
                        return false;
                if($scope.elem.res=="Radio")
                        return true;
                return false;
        };
        $scope.reload = function() {
                var len = q.length;
                for (var i = 0; i < len; i++) {
                        console.log($("#"+i).find("input"));
                }
        }
});
