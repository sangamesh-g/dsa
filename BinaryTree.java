import java.util.*;

public class BinaryTree{
    static class Node{
        int data;
        Node left,right;
        Node(int data){
            this.data=data;
            left=right=null;
        }
    }

    static class Tree{
        static int idx=-1;
        public static Node Buildtree(int node[]){
            idx++;
            if(node[idx]==-1){
                return null;
            }
            Node newnode=new Node(node[idx]);
            newnode.left=Buildtree(node);
            newnode.right=Buildtree(node);
            return newnode;
        }
    }
    public static void preorder(Node root){
        if(root==null){
            System.out.print("-1 ");
            return;
        }
        System.out.print(root.data+" ");
        preorder(root.left);
        preorder(root.right);
    }

    public static void inorder(Node root){
        if(root==null){
            System.out.print("-null node ");
            return;
        }
        inorder(root.left);
        System.out.print(root.data+" ");
        inorder(root.right);
    }
    public static int height(Node root){
	if(root==null){return 0;}
	int lhei=height(root.left);
	int rhei=height(root.right);
	return Math.max(lhei,rhei)+1;
}
    public static int countofnode(Node root){
        if(root==null){return 0;}
        int leftn=countofnode(root.left);
        int rightn=countofnode(root.right);
        return leftn+rightn+1;    }

    public static void levelorder(Node root){
        if(root==null){
            return;

        }
        Queue<Node> q=new LinkedList<>();
        q.add(root);

        while(!q.isEmpty()){
        int lvl=q.size();
        for(int i=0;i<lvl;i++){Node curr=q.remove();
	System.out.print(curr.data+" ");
	if(curr.left!=null){
        q.add(curr.left);
    }
	if(curr.right!=null){
        q.add(curr.right);
    }}
    System.out.println();
    }
}

    public static void postorder(Node root){
        if(root==null){
            System.out.print("-1 ");
            return;
        }
        postorder(root.left);
        postorder(root.right);
        System.out.print(root.data+"");
    }

    public static void main(String a[]){
        int node[]={1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1};
        Tree tree=new Tree();
        Node root=tree.Buildtree(node);
        // System.out.println(root.data);
        levelorder(root);
    }

}