/*! jQuery Page - v0.1 - 10-04-2014
* http://projects.irashid.com/frontend/jquery
* Copyright 2014 www.irashid.com; Licensed MIT */

 (function($) {

    $.fn.Page = function( options ) {

        // Establish our default settings
        var settings = $.extend({
            classes         : [],
            ids             : []
        }, options);

        var self = this;

        (function(){

            function getCamelCaseVariableNameFromString(string, wordSpliter ){

                var variableWordParts = string.split(wordSpliter);
                var variableName = "";
                $(variableWordParts).each(function(index, value){
                    variableName += value.ucfirst();
                });
                return variableName;
            }

            $(self.ids).each(function(index, value){

                var selectorName = getCamelCaseVariableNameFromString(value, "-");
                var idName = "#" + value;
                self[ 'get' + selectorName ] = function(){
                    return $(idName);
                }

                self['get' + selectorName + 'Id' ] = function(){
                    return idName;
                }

            });

            $(self.classes).each(function(index, value){

                var selectorName = getCamelCaseVariableNameFromString(value, "-");
                var className = "." + value;
                self[ 'get' + selectorName ] = function(){
                    return $(className);
                }

                self['get' + selectorName + 'Class' ] = function(){
                    return className;
                }

            });

        }());



    }

}(jQuery));
