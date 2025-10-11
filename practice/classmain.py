import threading
import dropboxuploadfilesession
import os
import queue


session_objects = []
q = queue.Queue()

def worker_thread():
    while not q.empty():
        file_path = q.get()
        dropbox_path = f"/NTTW_Demo/Photos/{os.path.basename(file_path)}"

        session = dropboxuploadfilesession.DropboxUploadFileSession(file_path, dropbox_path)
        session_objects.append(session)


file_path = os.path.join(os.path.dirname(__file__), "stephenrea.jpeg")
file_path2 = os.path.join(os.path.dirname(__file__), "brendanbehan.jpeg")
file_path3 = os.path.join(os.path.dirname(__file__), "jfk.jpeg")
files = [file_path, file_path2, file_path3]

for f in files:
    q.put(f)

num_threads = 2
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=worker_thread)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

for o in session_objects:
    print(f"{os.path.basename(o.FILE_PATH)} upload success? {o.SUCCESS}")
