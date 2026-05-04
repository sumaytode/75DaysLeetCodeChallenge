class Solution:
    def judgeCircle(self, moves: str) -> bool:
        U=moves.count('U')
        D=moves.count('D')
        L=moves.count('L')
        R=moves.count('R')

        vertical=U-D
        horizontal=L-R

        if vertical==0 and horizontal==0:
            return True
        else:
            return False
