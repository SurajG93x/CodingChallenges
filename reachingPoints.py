class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        if sx>tx or sy>ty:
            return False
        elif sx == tx:
            if (ty+sy)%sx == 0: return True
            else:  return False
        elif sy == ty:
            if (sx+tx)%sy == 0: return True
            else: return False
        else:
            return self.reachingPoints(sx+sy, sy, tx, ty) or self.reachingPoints(sx, sx+sy, tx, ty)

if __name__ == '__main__':
    f = Solution()
    print(f.reachingPoints(6, 3, 6, 15))