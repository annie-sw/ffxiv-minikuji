<template>
  <div>
    <table id="scratch-board" class="table table-bordered">
        <tbody>
            <tr>
                <th v-bind:class="[{ expected: classObject.expected_line_1 }, 'col-xs-1', 'col-sm-1']">1</th>
                <th v-bind:class="[{ expected: classObject.expected_line_2 }, 'col-xs-3', 'col-sm-3']">2</th>
                <th v-bind:class="[{ expected: classObject.expected_line_3 }, 'col-xs-3', 'col-sm-3']">3</th>
                <th v-bind:class="[{ expected: classObject.expected_line_4 }, 'col-xs-3', 'col-sm-3']">4</th>
                <th v-bind:class="[{ expected: classObject.expected_line_5 }, 'col-xs-1', 'col-sm-1']">5</th>
            </tr>
        <tr>
            <th v-bind:class="{ expected: classObject.expected_line_6 }">6</th>
            <td v-bind:class="{duplicated: classObject.duplicated_0, expected: classObject.expected_0}" v-on:click="selectIndex(0)">{{ dispNumber(0) }}</td>
            <td v-bind:class="{duplicated: classObject.duplicated_1, expected: classObject.expected_1}" v-on:click="selectIndex(1)">{{ dispNumber(1) }}</td>
            <td v-bind:class="{duplicated: classObject.duplicated_2, expected: classObject.expected_2}" v-on:click="selectIndex(2)">{{ dispNumber(2) }}</td>
        </tr>
        <tr>
            <th v-bind:class="{ expected: classObject.expected_line_7 }">7</th>
            <td v-bind:class="{duplicated: classObject.duplicated_3, expected: classObject.expected_3}" v-on:click="selectIndex(3)">{{ dispNumber(3) }}</td>
            <td v-bind:class="{duplicated: classObject.duplicated_4, expected: classObject.expected_4}" v-on:click="selectIndex(4)">{{ dispNumber(4) }}</td>
            <td v-bind:class="{duplicated: classObject.duplicated_5, expected: classObject.expected_5}" v-on:click="selectIndex(5)">{{ dispNumber(5) }}</td>
        </tr>
        <tr>
            <th v-bind:class="{ expected: classObject.expected_line_8 }">8</th>
            <td v-bind:class="{duplicated: classObject.duplicated_6, expected: classObject.expected_6}" v-on:click="selectIndex(6)">{{ dispNumber(6) }}</td>
            <td v-bind:class="{duplicated: classObject.duplicated_7, expected: classObject.expected_7}" v-on:click="selectIndex(7)">{{ dispNumber(7) }}</td>
            <td v-bind:class="{duplicated: classObject.duplicated_8, expected: classObject.expected_8}" v-on:click="selectIndex(8)">{{ dispNumber(8) }}</td>
            <th>
                <button class="btn btn-default" v-on:click="reset">Reset</button>
            </th>
        </tr>
        </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'scratch-board',
  data: function() {
    return {
      duplicatedIndexes: [],
    }
  },
  props: ['board', 'expectedIndexes', 'selectedLine'],
  computed: {
    classObject: function() {
      if (this.duplicatedIndexes.length > 0) {
        return this.getDuplicatedIndexClass(this.duplicatedIndexes)
      }
      if (this.expectedIndexes) {
        return this.getExpectedIndexClass(this.expectedIndexes)
      }
      if (this.selectedLine) {
        return this.getSelectedLineClass(this.selectedLine)
      }
      return {}
    },
  },

  methods: {

    // 表示する値を返す
    dispNumber: function(index) {
        var num = this.board[index]
        return num ? num : ''
    },

    // 初期化
    reset: function() {
      this.duplicatedIndexes = []
      this.$emit('reset')
    },

    // 重複チェック
    validate: function() {
      let indexes = []
      let values = this.board.filter((x, i, self) => {
          return x > 0 && self.indexOf(x) === i && i !== self.lastIndexOf(x)
        })
      this.board.forEach((v, i) => {
        if (values.indexOf(v) >= 0) {
          indexes.push(i)
        }
      })

      this.duplicatedIndexes = indexes

      return indexes.length == 0
    },

    // クリックイベント
    selectIndex: function(index) {
      // 重複値がある場合、他の場所は入力出来ないよ
      if (this.duplicatedIndexes.length > 0 && this.duplicatedIndexes.indexOf(index) < 0) {
        return
      }
      this.$emit('selectIndex', index, this.validate)  // 親へイベント通知
    },

    // 重複 classObject
    getDuplicatedIndexClass: function(duplicatedIndexes) {
      let ret = {}
      for (let i of duplicatedIndexes) {
        ret["duplicated_" + i] = true
      }
      return ret;
    },

    // 期待するインデックスの classObject
    getExpectedIndexClass: function(expectedIndexes) {
      let score = Math.max(...expectedIndexes.map(x => x.score))
      let ret = {}
      for (let x of expectedIndexes) {
        if (x.score == score)
          ret["expected_" + x.index] = true
      }
      return ret;
    },

    // 選択された列の classObject
    getSelectedLineClass: function(selectedLine) {
      let ret = {}
      let indexes = selectedLine['indexes']

      ret['expected_line_' + selectedLine['id']] = true
      indexes.forEach(function(i) {
        ret["expected_" + i] = true
      })
      return ret;
    },
  },
}
</script>

<style>
/* #scratch-board .selected { */
    /* color: #666666; */
    /* background-color: #ccffcc; */
/* } */
#scratch-board .duplicated {
    background-color: #ffcccc;
}
#scratch-board .expected {
    background-color: #ccffff;
}
#scratch-board th.expected {
    color: #666666;
}
/* #scratch-board .expected-2 { */
    /* background-color: #ccffcc; */
/* } */
#scratch-board th {
    text-align: center;
    vertical-align: middle;
    color: #ffffff;
    background-color: #666666;
    height: 60px;
}
#scratch-board td {
    text-align: center;
    vertical-align: middle;
}
#scratch-board {
    /* position: relative; */
}
</style>
