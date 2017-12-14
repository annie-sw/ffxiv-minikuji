<template>
  <div id="app">
    <ScratchBoard v-bind:board="board"
                  v-bind:expectedIndexes="expectedIndexes"
                  v-bind:selectedLine="selectedLine"
                  v-on:reset="reset"
                  v-on:selectIndex="selectIndex" />

    <ExpectedTable v-bind:expectedLines="expectedLines"
                   v-on:selectLine="selectLine" />

    <NumberPanels v-if="showNumberPanels"
                  v-bind:selectNumber="selectNumber" />
  </div>
</template>

<script>
import logic from './logic'
import ScratchBoard from './components/ScratchBoard'
import ExpectedTable from './components/ExpectedTable'
import NumberPanels from './components/NumberPanels'

export default {
  name: 'app',
  components: {
    ScratchBoard,
    ExpectedTable,
    NumberPanels,
  },
  data: function() {
    return {
      showNumberPanels: false,
      selectNumber: null,
      board: [],
      expectedIndexes: null,
      expectedLines: null,
      selectedLine: null,
    }
  },
  methods: {

    // 状態初期化
    reset: function() {
      this.board = logic.newBoard()
      this.expectedIndexes = null
      this.expectedLines = null
      this.selectedLine = null
    },

    // ScratchBoard のクリックイベント
    selectIndex: function(index, validate) {
      let getPhase = () => this.board.filter(x => x > 0).length

      // ４マス以上入力してたら、未入力のマスは入力出来ないよ
      if (getPhase() >= 4 && this.board[index] == 0) {
        return
      }

      this.showNumberPanels = true
      this.selectNumber = (number) => {  // NumberPanels のクリックイベント
        this.selectNumber =  null
        this.showNumberPanels = false

        if (number >= 0) {
          this.expectedIndexes = null
          this.expectedLines = null
          this.selectedLine = null

          this.board.splice(index, 1, number)
          if (validate()) {
            this.calcExpection(getPhase())
          }
        }
      }
    },

    // ExpectedTable のクリックイベント
    selectLine: function(lineId) {
      this.selectedLine = {
        id: lineId,
        indexes: logic.consts.lines[lineId],
      }
    },

    // 候補の選出
    calcExpection: function(phase) {
      if (phase < 4) {
        // パネル単位でスコアリング
        this.expectedIndexes = logic.calcHigherExpectedIndex(this.board)
      }
      else {
        // 列単位でスコアリング
        let ret = {}
        for (let line_id in logic.consts.lines) {
          let values = logic.getExpectedScores(this.board, line_id).sort((a,b) => b-a);
          ret[line_id] = {
            score: logic.sum(values) * 100 / values.length / 100,
            values: values,
          }
        }
        this.expectedLines = ret
      }
    },
  },

  // 初期化
  mounted: function() {
    this.reset()
  }
}
</script>

<style>
</style>
