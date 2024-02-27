"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _toPropertyKey(t) { var i = _toPrimitive(t, "string"); return "symbol" == _typeof(i) ? i : String(i); }
function _toPrimitive(t, r) { if ("object" != _typeof(t) || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || "default"); if ("object" != _typeof(i)) return i; throw new TypeError("@@toPrimitive must return a primitive value."); } return ("string" === r ? String : Number)(t); }
function _callSuper(t, o, e) { return o = _getPrototypeOf(o), _possibleConstructorReturn(t, _isNativeReflectConstruct() ? Reflect.construct(o, e || [], _getPrototypeOf(t).constructor) : o.apply(t, e)); }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _isNativeReflectConstruct() { try { var t = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); } catch (t) {} return (_isNativeReflectConstruct = function _isNativeReflectConstruct() { return !!t; })(); }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
var Header = /*#__PURE__*/function (_React$Component) {
  _inherits(Header, _React$Component);
  function Header() {
    _classCallCheck(this, Header);
    return _callSuper(this, Header, arguments);
  }
  _createClass(Header, [{
    key: "render",
    value: function render() {
      console.log(this.props.title); // dışardan değişken alamaya yarar htmlden
      console.log(this.props.numberList);
      return /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("h1", null, this.props.title), /*#__PURE__*/React.createElement(ToDoList, {
        numberList: this.props.numberList
      }));
    }
  }]);
  return Header;
}(React.Component); //yeni bir tag gibi düşünebilirsin
/*function Header(props){
    console.log(props.title);
        return (
            <div>
                <h1>`${props.title}`</h1>
                <h2>tamam</h2>
            </div>
        );
    } // burda htmlden değişken almaya yarar
*/
var ToDoList = /*#__PURE__*/function (_React$Component2) {
  _inherits(ToDoList, _React$Component2);
  function ToDoList(props) {
    var _this;
    _classCallCheck(this, ToDoList);
    _this = _callSuper(this, ToDoList, [props]);
    _this.clearItems = _this.clearItems.bind(_assertThisInitialized(_this)); //this e yeniden sahip olmak için
    _this.degerDegistir = _this.degerDegistir.bind(_assertThisInitialized(_this));
    _this.state = {
      numara: _this.props.numberList[0]
    };
    return _this;
  }
  _createClass(ToDoList, [{
    key: "degerDegistir",
    value: function degerDegistir() {
      //this.state.numara = "11"; 
      // bunun yerine html de değişsin diye
      // state olmak zorunda
      this.setState({
        numara: "1"
      });
    }
  }, {
    key: "clearItems",
    value: function clearItems() {
      console.log(this.props);
    }
  }, {
    key: "render",
    value: function render() {
      console.log(this.props.numberList);
      return /*#__PURE__*/React.createElement("div", null, this.props.numberList.map(function (item, index) {
        return /*#__PURE__*/React.createElement("li", {
          key: index
        }, " ", item);
      }), /*#__PURE__*/React.createElement("button", {
        onClick: this.clearItems
      }, " temizle "), /*#__PURE__*/React.createElement("button", {
        onClick: this.degerDegistir
      }, " degistir "), /*#__PURE__*/React.createElement("p", null, this.state.numara));
    }
  }]);
  return ToDoList;
}(React.Component);
var Action = /*#__PURE__*/function (_React$Component3) {
  _inherits(Action, _React$Component3);
  function Action() {
    _classCallCheck(this, Action);
    return _callSuper(this, Action, arguments);
  }
  _createClass(Action, [{
    key: "onFromSumbmit",
    value: function onFromSumbmit(event) {
      event.preventDefault();
      var a = event.target.elements.isim.value;
      console.log(a);
    }
  }, {
    key: "render",
    value: function render() {
      return /*#__PURE__*/React.createElement("form", {
        onSubmit: this.onFromSumbmit
      }, /*#__PURE__*/React.createElement("input", {
        type: "text",
        name: "isim"
      }), /*#__PURE__*/React.createElement("button", {
        type: "submit"
      }, " add item "));
    }
  }]);
  return Action;
}(React.Component);
var ToDoApp = /*#__PURE__*/function (_React$Component4) {
  _inherits(ToDoApp, _React$Component4);
  function ToDoApp() {
    _classCallCheck(this, ToDoApp);
    return _callSuper(this, ToDoApp, arguments);
  }
  _createClass(ToDoApp, [{
    key: "render",
    value: function render() {
      this.naber = "a";
      var numberList = ["10", "20", "30", "40"];
      var title = "asdf";
      return /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(Header, {
        title: title,
        numberList: numberList
      }), /*#__PURE__*/React.createElement(Action, null));
    }
  }]);
  return ToDoApp;
}(React.Component); // her şeyi buraya koyuyoruz
ReactDOM.render( /*#__PURE__*/React.createElement(ToDoApp, null), document.getElementById('root'));
