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
    reset: function() {
      this.board = logic.newBoard()
      this.expectedIndexes = null
      this.expectedLines = null
      this.selectedLine = null
    },

    selectIndex: function(index, validate) {
      let getPhase = () => this.board.filter(x => x > 0).length
      if (getPhase() >= 4 && this.board[index] == 0) {
        return
      }

      this.showNumberPanels = true
      this.selectNumber = (number) => {
        this.selectNumber =  null
        this.showNumberPanels = false

        this.expectedIndexes = null
        this.expectedLines = null
        this.selectedLine = null

        if (number >= 0) {
          this.board.splice(index, 1, number)
          if (validate()) {
            this.calcExpection(getPhase())
          }
        }
      }
    },

    selectLine: function(lineId) {
      this.selectedLine = {
        id: lineId,
        indexes: logic.consts.lines[lineId],
      }
    },

    calcExpection: function(phase) {
      if (phase < 4) {
        this.expectedIndexes = logic.calcHigherExpectedIndex(this.board)
      } else {
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
  mounted: function() {
    this.reset()
  }
}
</script>

<style>
</style>
