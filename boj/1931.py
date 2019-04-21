import sys

n = int(sys.stdin.readline())

meeting = []

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    meeting.append((e, s))

meeting.sort()

ans = 0
prevMeetingEndTime = 0
for i in meeting:
    end, start = i
    if start >= prevMeetingEndTime:
        ans += 1
        prevMeetingEndTime = end

print(ans)